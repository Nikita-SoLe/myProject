import os
import io
import aiofiles
from aiogram import Router, F, types
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext

from fsm.base import FSM_Main, Download
from download.you_tube import download_video
from keyboards.main_kb import main_menu_kb

router = Router()


#
@router.message(Text('Видео'))
async def dwn_video(message: types.Message, state: FSMContext):
    await state.set_state(Download.video)
    await message.answer('Отправьте ссылку на видео',
                         reply_markup=main_menu_kb())


@router.message(Text('Аудио'))
async def dwn_video(message: types.Message, state: FSMContext):
    await state.set_state(Download.audio)
    await message.answer('Отправьте ссылку на видео\n'
                         'С которого хотите скачать аудиодорожку',
                         reply_markup=main_menu_kb())


@router.message(Download.video, F.text)
async def handle_download_video(message: types.Message, state: FSMContext):
    await message.answer('Подождите немного пожалуйста')
    video_url = message.text
    output_directory = "/home/nikita/PycharmProjects/myProject/video/"

    # Скачивание видео
    video_filename = download_video(video_url, type='video')

    # отправка видео
    if video_filename:
        file_path = output_directory + video_filename

        save_to_io = io.BytesIO()
        async with aiofiles.open(file_path, 'rb') as f:
            video_bytes = await f.read()

            save_to_io.write(video_bytes)
            save_to_io.seek(0)

        r = save_to_io.getvalue()
        input_file_d = types.BufferedInputFile(r,
                                               filename=output_directory)
        await message.answer_video(input_file_d, caption='Вот ваше видео', reply_markup=main_menu_kb())

        # Удаление скачанного видео
        os.remove(file_path)
        await state.set_state(Download.video)

    else:
        await message.reply("Не удалось скачать видео.\n"
                            "Проверьте ссылку",
                            reply_markup=main_menu_kb())

    await state.set_state(Download.video)


#
@router.message(Download.audio, F.text)
async def handler_download_audio(message: types.Message, state: FSMContext):
    await message.answer('Подождите немного пожалуйста')
    audio_url = message.text
    output_directory = "/home/nikita/PycharmProjects/myProject/audio/"

    # Скачивание аудио
    audio_filename = download_video(audio_url, type='audio')

    # отправка аудио
    if audio_filename:

        file_path = output_directory + audio_filename

        save_to_io = io.BytesIO()
        async with aiofiles.open(file_path, 'rb') as f:
            video_bytes = await f.read()

            save_to_io.write(video_bytes)
            save_to_io.seek(0)

        r = save_to_io.getvalue()
        input_file_d = types.BufferedInputFile(r,
                                               filename=output_directory)
        await message.answer_audio(input_file_d, caption='Вот ваше аудио', reply_markup=main_menu_kb())

        # Удаление скачанного аудио
        os.remove(file_path)
        await state.set_state(Download.audio)

    else:
        await message.reply("Не удалось скачать аудио.\n"
                            "Проверьте ссылку",
                            reply_markup=main_menu_kb())

    await state.set_state(Download.audio)
