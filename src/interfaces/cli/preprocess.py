from src.application.use_cases.preprocess_dataset import preprocess_and_save
from src.config import settings


def main():
    path = preprocess_and_save()
    print(f"saved: {path}")


if __name__ == "__main__":
    main()
