from PIL import Image
import pillow_heif
import os

def convert_heic_to_png(input_path, output_path):
    """
    将指定目录中的 HEIC 文件转换为 PNG 格式。
    
    参数:
        input_path (str): 包含 HEIC 文件的输入目录
        output_path (str): 保存 PNG 文件的输出目录
    """
    # 确保输出目录存在
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # 遍历输入目录中的文件
    for filename in os.listdir(input_path):
        if filename.lower().endswith('.heic'):
            # 构建输入和输出文件的完整路径
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, os.path.splitext(filename)[0] + '.png')
            
            try:
                # 读取 HEIC 文件
                heif_file = pillow_heif.read_heif(input_file)
                
                # 将 HEIF 文件转换为 PIL Image 对象
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw",
                    heif_file.mode,
                    heif_file.stride,
                )
                
                # 保存为 PNG 格式
                image.save(output_file, 'PNG')
                print(f"已转换: {input_file} -> {output_file}")
                
            except Exception as e:
                print(f"转换 {input_file} 时出错: {e}")

if __name__ == "__main__":
    # 指定输入和输出目录
    input_directory = "/Users/weitaikang/Desktop/WeitaiKang.github.io/experiences/travel/"  # 替换为你的 HEIC 文件目录
    output_directory = "/Users/weitaikang/Desktop/WeitaiKang.github.io/experiences/travel/"  # 替换为输出 PNG 文件的目录
    
    # 调用转换函数
    convert_heic_to_png(input_directory, output_directory)