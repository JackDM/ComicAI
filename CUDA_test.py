import os
import torch

def check_env():
    print("\nVariables de entorno relacionadas con CUDA:")
    for var in ["CUDA_HOME", "CUDA_PATH", "PATH"]:
        if var in os.environ:
            print(f"{var}: {os.environ[var]}")

def check_cuda():
    print(f"Versión de PyTorch: {torch.__version__}")
    print(f"Versión de CUDA desde PyTorch: {torch.version.cuda}")
    print(f"Versión de cuDNN desde PyTorch: {torch.backends.cudnn.version()}")
    print(f"CUDA disponible: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"Nombre del dispositivo: {torch.cuda.get_device_name(0)}")
        print(f"Número de GPUs disponibles: {torch.cuda.device_count()}")

if __name__ == "__main__":
    check_env()
    check_cuda()