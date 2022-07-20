from yt_dlp import YoutubeDL

# Download Udemy course keeping each chapter in separate directory under MyVideos directory in your home
# $ yt-dlp -u user -p password -P "~/MyVideos" -o "%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s" "https://www.udemy.com/java-tutorial"

course = "https://www.udemy.com/course/analyse-et-visualisation-de-data-avec-python"

YoutubeDL.download(url_list=course)pythg