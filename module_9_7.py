def is_prime(func) :
    def wrapper(*args) :
        sum_ = func(*args)

        if sum_ < 2:
            print(f"Незадача: результат сложения не является ни простым, ни составным числом")
            return

        flag = True

        for i in range(2, sum_ - 1) :
            if sum_ % i == 0 :
                flag = False
                break
        if flag :
                print('Простое')
        else:
                print('Составное')
        return sum_
    return wrapper

@is_prime
def sum_three(*args) :
    return sum(args)

result = sum_three(2,3,6)
print(result)
