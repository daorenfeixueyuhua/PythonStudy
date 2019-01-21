from retrying import retry


@retry(stop_man_attempt_number =3 )
def fun():
    print("this is fun1")
    raise ValueError("this is test error")


fun()
