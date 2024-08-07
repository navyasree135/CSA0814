n= 3*3
matrix = [[1,2,3],[4,5,6],[7,8,9]]
diag_elements = [matrix[i][i] for i in range(len(matrix))]
sum_diagonal=sum(diag_elements)
print(f"Diagonal elements: {diag_elements}, Sum: {sum_diagonal}")