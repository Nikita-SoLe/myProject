from aiogram import Router, Bot, types


router: Router = Router()


@router.pre_checkout_query()
async def process_pre_checkout_query(query: types.PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(query.id, ok=True)


@router.message(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    print('SUCCESSFUL PAYMENT:')
    payment_info = message.successful_payment
    print(f"Currency: {payment_info.currency}")
    print(f"Total amount: {payment_info.total_amount}")
    print(f"Invoice payload: {payment_info.invoice_payload}")
    await message.answer(f'Платеж на сумму {payment_info.total_amount // 100} {payment_info.currency} прошел успешно!!!')
