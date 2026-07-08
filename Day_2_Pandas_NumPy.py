import numpy as np
import pandas as pd


def pandas_methods_demo():
    print("\n=== Pandas: 10 methods on CSV data ===")
    df = pd.read_csv("data/tips.csv")

    # 1
    print("\n1) head()")
    print(df.head(3))

    # 2
    print("\n2) tail()")
    print(df.tail(3))

    # 3
    print("\n3) info()")
    df.info()

    # 4
    print("\n4) describe()")
    print(df.describe()) #df.describe()
    #This gives a quick summary of numeric columns in your CSV, like:
    #total values (count)
    #average (mean)
    #spread (std)
    #smallest (min)
    #middle value (50%)
    #largest (max)
    #Think of it as: “Show me the overall health/report card of my numeric data.”

    # 5
    print("\n5) shape")
    print(df.shape)

    # 6
    print("\n6) columns")
    print(df.columns.tolist())

    # 7
    print("\n7) isnull().sum()")
    print(df.isnull().sum())#df.isnull().sum()
    #This checks missing data in each column.

    #isnull() makes True/False values (True = missing)
    #sum() counts how many True are there per column
    #Think of it as: “Tell me how many blank cells each column has.”

    # 8
    print("\n8) value_counts() on 'day'")
    print(df["day"].value_counts())

    # 9
    print("\n9) groupby('sex')['total_bill'].mean()")
    print(df.groupby("sex")["total_bill"].mean())

    # 10
    print("\n10) sort_values('total_bill', ascending=False)")
    print(df.sort_values("total_bill", ascending=False).head(5))


def numpy_methods_demo():
    print("\n=== NumPy: multidimensional arrays and 15 methods ===")

    arr2d = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
    arr2d_b = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])

    print("\nOriginal 2D Array:")
    print(arr2d)

    print("\nIndex access:")
    print("arr2d[0, 1] =", arr2d[0, 1])
    print("arr2d[2, 2] =", arr2d[2, 2])

    print("\nMath operations using indices:")
    print("arr2d[0,0] + arr2d[1,1] =", arr2d[0, 0] + arr2d[1, 1])
    print("arr2d[2,2] - arr2d[0,2] =", arr2d[2, 2] - arr2d[0, 2])
    print("arr2d[1,0] * arr2d[2,1] =", arr2d[1, 0] * arr2d[2, 1])
    print("arr2d[2,0] / arr2d[0,0] =", arr2d[2, 0] / arr2d[0, 0])

    # 15 NumPy methods/examples
    print("\n1) np.zeros((2, 3))")
    print(np.zeros((2, 3)))#Creates a 2 rows × 3 columns array filled with 0.

    print("\n2) np.ones((2, 2))")
    print(np.ones((2, 2)))#Creates a 2 rows × 2 columns array filled with 1.

    print("\n3) np.arange(0, 10, 2)")
    print(np.arange(0, 10, 2))#Creates an array of numbers from 0 to 9, with a step of 2.

    print("\n4) np.linspace(1, 5, 5)")
    print(np.linspace(1, 5, 5))#Creates an array of 5 numbers evenly spaced between 1 and 5.

    print("\n5) np.reshape(arr2d, (1, 9))")
    print(np.reshape(arr2d, (1, 9)))#Reshapes the 2D array into a 1 row × 9 columns array.

    print("\n6) np.transpose(arr2d)")
    print(np.transpose(arr2d))#Transposes the array, swapping rows and columns.

    print("\n7) np.sum(arr2d)")
    print(np.sum(arr2d))#Sums all elements in the array.

    print("\n8) np.mean(arr2d)")
    print(np.mean(arr2d))#Calculates the average of all elements in the array.

    print("\n9) np.max(arr2d)")
    print(np.max(arr2d))#Finds the maximum value in the array.

    print("\n10) np.min(arr2d)")
    print(np.min(arr2d))#Finds the minimum value in the array.

    print("\n11) np.sqrt(arr2d)")
    print(np.sqrt(arr2d))#Calculates the square root of each element in the array.

    print("\n12) np.concatenate((arr2d, arr2d_b), axis=0)")
    print(np.concatenate((arr2d, arr2d_b), axis=0))#Concatenates the two arrays along the rows (axis=0).

    print("\n13) np.vstack((arr2d, arr2d_b))")
    print(np.vstack((arr2d, arr2d_b)))#Vertically stacks the two arrays.    

    print("\n14) np.hstack((arr2d, arr2d_b))")
    print(np.hstack((arr2d, arr2d_b)))#Horizontally stacks the two arrays.

    print("\n15) np.dot(arr2d, np.transpose(arr2d_b))")
    print(np.dot(arr2d, np.transpose(arr2d_b)))#Calculates the dot product of the two arrays.


if __name__ == "__main__":
    pandas_methods_demo()
    numpy_methods_demo()
