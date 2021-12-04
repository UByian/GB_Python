users = ["John", "Artur", "Kate"]


    def say_hello(*user_list):
        for user in user_list:
            print(user)

    say_hello(*users)
