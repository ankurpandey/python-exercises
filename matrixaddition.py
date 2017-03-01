# program for n x n matrix addition
rows = int(input('Enter rows:'))
columns = int(input('Enter columns:'))

def addMatrix(matrix1,matrix2):
	matrix = initializeMatrix()
	for i in range(rows):
		for j in range(columns):
			matrix[i][j] = matrix1[i][j] + matrix2[i][j]
	return matrix

def valueInput():
	matrix = [[int(input()) for j in range(columns)] for i in range(rows)]
	return matrix

def initializeMatrix():
	matrix = [[0 for j in range(columns)] for i in range(rows)]
	return matrix

def main():
	matrix1 = initializeMatrix()
	print('Enter matrix1 value:')
	matrix1 = valueInput()

	matrix2 = initializeMatrix()
	print('Enter matrix2 value:')
	matrix2 = valueInput()

	result = addMatrix(matrix1,matrix2)
	
	print('matrix one:',matrix1)
	print('matrix two:',matrix2)
	print('matrix add:',result)
	
if __name__ == '__main__':
	main()
	