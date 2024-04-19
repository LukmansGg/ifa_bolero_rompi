from googlesearch import search



def search(query):
    try:
        for i in search(query, num_results=20, lang='id', advanced=True):
            string_result = str(i)

            title_raw = string_result.split("title=")[1]
            title_result = title_raw.split(", description")[0]
            description_raw = string_result.split("description=")[1]
            description_result = description_raw.split(")")[0]

            link_raw = string_result.split("url=")[1]
            link_result = link_raw.split(", title")[0]
            my_results_list.append(link_result)

        bot.sendMessage(
            chat_id,
            f"[1/20]\nHasil Pencarian: [{title_result}]\n\n{description_result}\nsumber: {my_results_list[0]}\n\npower by [googlesearch]",
            reply_markup = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="next",callback_data='next_search')]
            ])
        )
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 429:
            # Tambahkan penundaan sebelum mencoba lagi
            time.sleep(5)  # Contoh penundaan 5 detik, sesuaikan sesuai kebutuhan
            # Coba kembali permintaan setelah penundaan
            bot.sendMessage(
                chat_id,
                "Maaf, saat ini sedang terdapat gangguan pada sistem jaringan Google kami 🙏"
            )
    except TelegramError as err:
        pass