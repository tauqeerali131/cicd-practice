def health_check():
    return "OK"


def get_environment():
    return "production"


if __name__ == "__main__":
    print("Application status:", health_check())
    print("Environment:", get_environment())
