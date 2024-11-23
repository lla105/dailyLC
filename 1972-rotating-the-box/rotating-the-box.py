from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)  # Number of rows
        n = len(box[0])  # Number of columns
        
        # Step 1: Process each row to simulate stones falling down
        for row in box:
            write_pos = len(row) - 1  # Position to write the next stone
            for j in range(len(row) - 1, -1, -1):  # Iterate right-to-left
                if row[j] == '#':  # If it's a stone, move it to `write_pos`
                    row[write_pos] = '#'
                    if write_pos != j:
                        row[j] = '.'
                    write_pos -= 1
                elif row[j] == '*':  # Obstacle resets the `write_pos`
                    write_pos = j - 1

        # Step 2: Rotate the box to the right
        # Rotating a matrix 90 degrees clockwise means turning rows into columns
        rotated_box = []
        for j in range(n):  # Columns of the original box
            new_row = []
            for i in range(m - 1, -1, -1):  # Traverse rows bottom-to-top
                new_row.append(box[i][j])
            rotated_box.append(new_row)
        
        return rotated_box
