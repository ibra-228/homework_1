import time
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def is_admin_with_kwargs(func):
    def wrapper(*args, **kwargs):
        user = kwargs["x"]
        if user.role.lower() == "admin":
            return func(*args, **kwargs)
        else:
            print("У вас нет доступа")
            return None

    return wrapper


def is_admin(func):
    def wrapper(*args):
        user = args[0]
        if user.role == "admin".lower():
            return func(*args)
        else:
            print("У вас нет доступа")
            return None
    return wrapper

@is_admin
def delete_video(user):
    print("Видео удалено")


@is_admin_with_kwargs
def delete_video_with_kwargs(x):
    print("Видео удалено")

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exe_time = end_time - start_time
        print(f'Время выполнения: {exe_time:.1f} секунд')
        return result
    return wrapper

@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")

admin = User("Ardager", "admin")
user1 = User("Bek", "user")

delete_video(user1)
delete_video_with_kwargs(x=admin)

download_video()





