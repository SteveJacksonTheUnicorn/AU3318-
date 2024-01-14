from config import *

#进行图片的复制拼接
def concat_images(image_names, name, path):
    image_files = []
    for index in range(COL*ROW):
        image_files.append(Image.open(os.path.join(path, image_names[index]))) #读取所有用于拼接的图片
    target = Image.new('RGB', (UNIT_WIDTH_SIZE * COL, UNIT_HEIGHT_SIZE * ROW)) #创建成品图的画布
    #第一个参数RGB表示创建RGB彩色图，第二个参数传入元组指定图片大小，第三个参数可指定颜色，默认为黑色
    for row in range(ROW):
        for col in range(COL):
            #对图片进行逐行拼接
            #paste方法第一个参数指定需要拼接的图片，第二个参数为二元元组（指定复制位置的左上角坐标）
            #或四元元组（指定复制位置的左上角和右下角坐标）
            target.paste(image_files[COL*row+col], (0 + UNIT_WIDTH_SIZE*col, 0 + UNIT_HEIGHT_SIZE*row))
    target.save(name + '.png', quality=SAVE_QUALITY) #成品图保存

#获取需要拼接图片的名称
def get_image_names(path):
    selected_images = []
    for i in range(1,11):
        num = i*400
        selected_images.append("FFT=2^14/{}raw.png".format(num))
    return selected_images


if __name__ == '__main__':
    # 图片拼接
    COL = 2 #指定拼接图片的列数
    ROW = 5 #指定拼接图片的行数
    UNIT_HEIGHT_SIZE = 400 #图片高度
    UNIT_WIDTH_SIZE = 1200 #图片宽度
    PATH = "f_analysis_superposition" #需要拼接的图片所在的路径
    NAME = "f_analysis_superposition" #拼接出的图片保存的名字
    SAVE_QUALITY = 50 #保存的图片的质量 可选0-100
    concat_images(get_image_names(PATH), NAME, PATH)

    