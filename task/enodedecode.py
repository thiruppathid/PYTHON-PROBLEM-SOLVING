class Solution:
    def decode_ciphertext(self, encoded_text: str, rows: int) -> str:
        # Initialize a list to hold the decoded characters
        decoded_characters = []
      
        # Calculate the number of columns based on the length of the encoded text and number of rows
        cols = len(encoded_text) // rows
      
        # Iterate over each column index starting from 0
        for col_index in range(cols):
            # Initialize starting point
            row, col = 0, col_index
          
            # Traverse the encoded text by moving diagonally in the matrix
            # constructed by rows and columns
            while row < rows and col < cols:
                # Determine the linear index for the current position in the (row, col) matrix
                linear_index = row * cols + col
              
                # Append the corresponding character to the decoded list
                decoded_characters.append(encoded_text[linear_index])
              
                # Move diagonally: go to next row and next column
                row, col = row + 1, col + 1
      
        # Join the decoded characters to form the decoded string.
        # Strip trailing spaces if any.
        return ''.join(decoded_characters).rstrip()
obj=Solution()
#s=input()
print(obj.decode_ciphertext(input(),int(input())))