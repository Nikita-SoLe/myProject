from pytube import YouTube
import uuid


# Возвращает аудио или видео
def download_video(url, type, res='480p'):
    yt = YouTube(url)
    file_id = uuid.uuid4().fields[-1]
    if type == 'audio':
        audio_stream = yt.streams.get_audio_only()
        if audio_stream:
            audio_stream.download("audio", f"{file_id}.mp3")
            return f"{file_id}.mp3"
        else:
            print("Видео не содержит аудио.")
            return None
    elif type == 'video':
        video_stream = yt.streams.filter(res=res, progressive=True).first()
        if video_stream:
            video_stream.download("video", f"{file_id}.mp4")
            return f"{file_id}.mp4"
        else:
            print("Не удалось найти видео-стрим с выбранным разрешением. Скачивается видео с наивысшим разрешением.")
            highest_resolution_stream = yt.streams.get_highest_resolution()
            if highest_resolution_stream:
                highest_resolution_stream.download("video", f"{file_id}.mp4")
                return f"{file_id}.mp4"
            else:
                print("Не удалось найти видео-стрим с наивысшим разрешением.")
                return None
    else:
        print("False")
        return None


if __name__ == '__main__':
    download_video('https://youtube.com/shorts/JxSrpc43m1Q?feature=share', type='video')
