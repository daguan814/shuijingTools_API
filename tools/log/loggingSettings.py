import logging
from colorlog import ColoredFormatter

# 移除根日志记录器的默认处理程序
logging.getLogger('').handlers = []

# 创建文件处理程序
file_handler = logging.FileHandler(filename='./tools/log/log.txt')
file_handler.setLevel(logging.WARNING)  # 设定日志输出级别
file_handler.setFormatter(logging.Formatter('[%(levelname)s] %(asctime)s - %(message)s'))

# 创建并配置控制台处理程序
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = ColoredFormatter(
    '%(log_color)s[%(levelname)s] %(asctime)s - %(message)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)
console_handler.setFormatter(formatter)

# 添加文件和控制台处理器到根日志记录器
logging.getLogger('').addHandler(file_handler)
logging.getLogger('').addHandler(console_handler)

# 设置根日志记录器的级别
logging.getLogger('').setLevel(logging.INFO)

# 创建日志记录器
logger = logging.getLogger(__name__)

# 此时，控制台只会输出一次，同时也会写入到文件中
# logger.info("This message will be logged both in the console and the log file.")
