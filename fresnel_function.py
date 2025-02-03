# import numpy as np
# from scipy.integrate import quad
# from scipy.optimize import fsolve

# # 주어진 함수
# def integrand(x):
#     return np.sin(0.5 * np.pi * x**2)

# # u에 대한 적분 함수 정의
# def integral(u):
#     result, _ = quad(integrand, 0, u)
#     return result

# # 목표 함수 정의: 이 함수의 0을 찾으면 됩니다.
# def target_function(u):
#     return integral(u) - 0.2

# # 초기 추정값으로 fsolve 함수를 사용하여 u를 계산
# u_solution = fsolve(target_function, 0.5)  # 0.5는 초기 추정값입니다.

# print("u의 계산된 값:", u_solution[0])
# import numpy as np
# from scipy.integrate import quad
# from scipy.optimize import fsolve

# # 주어진 함수
# def integrand(x):
#     return np.sin(0.5 * np.pi * x**2)

# # u에 대한 적분 함수 정의
# def integral(u):
#     result, _ = quad(integrand, 0, u)
#     return result

# # 목표 함수 정의: 이 함수의 0을 찾으면 됩니다.
# def target_function(u):
#     return integral(u) - 0.2

# # 초기 추정값으로 fsolve 함수를 사용하여 u를 계산
# u_solution = fsolve(target_function, 0.5)  # 0.5는 초기 추정값입니다.

# print("u의 계산된 값:", u_solution[0])

name = "amy"
print("Hello %s"%name)