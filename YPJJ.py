import os
from pydub import AudioSegment

# 手动设置FFmpeg路径
AudioSegment.converter = r'C:\Program Files\ffmpeg\bin\ffmpeg.exe'

# 定义剪辑的秒数
CLIP_START_SECONDS = 15  # 剪掉前15秒
CLIP_END_SECONDS = 20    # 剪掉后20秒

# 音频文件夹路径
AUDIO_FOLDER = r'G:\音频剪辑\Before'
# 输出文件夹路径
OUTPUT_FOLDER = r'G:\音频剪辑\After'

# 确保输出文件夹存在
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# 获取所有.m4a音频文件
audio_files = [f for f in os.listdir(AUDIO_FOLDER) if f.endswith('.m4a')]

for audio_file in audio_files:
    try:
        # 读取音频文件
        audio_path = os.path.join(AUDIO_FOLDER, audio_file)
        audio = AudioSegment.from_file(audio_path, format="m4a")
        
        # 计算剪辑后的音频长度
        start_trim = CLIP_START_SECONDS * 1000
        end_trim = CLIP_END_SECONDS * 1000
        duration = len(audio)
        trimmed_audio = audio[start_trim:duration-end_trim]
        
        # 输出剪辑后的音频文件，保留原文件名
        output_path = os.path.join(OUTPUT_FOLDER, audio_file)
        trimmed_audio.export(output_path, format="mp4", codec="aac")  # 使用AAC编码，输出为mp4格式
        print(f"剪辑完成: {audio_file} -> {output_path}")
    
    except Exception as e:
        print(f"处理文件 {audio_file} 时出错: {e}")

print(f"批量音频剪辑完成，剪辑后的文件保存在 {OUTPUT_FOLDER} 文件夹中。")
