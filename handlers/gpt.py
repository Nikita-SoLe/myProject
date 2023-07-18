import openai
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from fsm.base import FSM_Main
from keyboards.main_kb import main_menu_kb
from config_reader import config

router = Router()
openai.api_key = config.gpt_token.get_secret_value()


#
@router.message(FSM_Main.chat_gpt, F.text)
async def gpt_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    chat_history = data.get("chat_history", [])

    user_message_id = None
    user_message_user_id = None

    if chat_history:
        #
        user_message = chat_history[-1]
        user_message_text = user_message['text']
        user_message_id = user_message['message_id']
        user_message_user_id = user_message['user_id']

        #
        chat_history.append({
            'text': message.text,
            'message_id': message.message_id,
            'user_id': message.from_user.id
        })
    else:
        #
        chat_history.append({
            'text': message.text,
            'message_id': message.message_id,
            'user_id': message.from_user.id
        })

    chat_history_text = '\n'.join([msg['text'] for msg in chat_history])

    try:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=chat_history_text,
            temperature=0.5,
            max_tokens=500,
            n=1,
            stop=None,
            echo=True
        )
        reply = response.choices[0].text.strip()

        #
        await message.answer(reply,
                             reply_to_message_id=user_message_id,
                             user_id=user_message_user_id,
                             reply_markup=main_menu_kb())

        await state.set_state(data)
    except openai.OpenAIError as e:
        await message.answer(f'Произошла ошибка при обращении к ChatGPT: {str(e)}',
                             reply_markup=main_menu_kb())

    await state.set_state(FSM_Main.chat_gpt)

