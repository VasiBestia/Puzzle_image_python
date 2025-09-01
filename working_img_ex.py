from PIL import Image

mask = Image.open("mask.png")
mask2 = mask.resize((1015, 559))
maskfinal = mask2.copy()
maskfinal.putalpha(50)
maskfinal.show()

matrix = Image.open("word_matrix.png")
matrix.paste(maskfinal, (0, 0), mask=maskfinal)
matrix.show()
matrix.save("word_matrix_solution.png")
