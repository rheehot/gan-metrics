from enum import Enum, unique


@unique
class DeviceType(str, Enum):
    CPU = 'cpu'
    GPU = 'cuda'


@unique
class ModelType(str, Enum):
    INCEPTION_V2 = 'inception_v2'
    INCEPTION_V3 = 'inception_v3'


@unique
class MetricType(str, Enum):
    IS = 'inception_score'
    FID = 'fid'
    LPIPS = 'lpips'
    PPL = 'ppl'
    PSNR = 'psnr'
    SSIM = 'ssim'
