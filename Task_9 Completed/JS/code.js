document.getElementById('generateButton').addEventListener('click', () => {
    const num = parseInt(document.getElementById('numberInput').value);
    if (!num || num <= 0) {
        alert('Please enter a valid positive number.');
        return;
    }

    const row = Math.floor(Math.sqrt(num));
    const column = Math.ceil(num / row);
    const matrix = generateMatrix(row, column);

    displayMatrix(matrix);

    const botNumber = botSelectFromOuterLayer(matrix);
    const numberToFind = chooseRandomNumberInMatrix(matrix);

    const path = findPath(matrix, botNumber, numberToFind);
    if (path) {
        document.getElementById('result').innerText = `Path found: ${path.join(' -> ')}`;
        highlightPath(matrix, path);
    } else {
        document.getElementById('result').innerText = 'No path found to the destination number.';
    }
});

function generateMatrix(rows, cols) {
    const matrix = [];
    for (let i = 0; i < rows; i++) {
        const row = [];
        for (let j = 0; j < cols; j++) {
            row.push(Math.floor(Math.random() * 100) + 1);
        }
        matrix.push(row);
    }
    return matrix;
}

function displayMatrix(matrix) {
    const matrixDiv = document.getElementById('matrix');
    matrixDiv.innerHTML = '';
    matrixDiv.style.gridTemplateRows = `repeat(${matrix.length}, 1fr)`;
    matrixDiv.style.gridTemplateColumns = `repeat(${matrix[0].length}, 1fr)`;
    
    matrix.forEach(row => {
        row.forEach(cell => {
            const cellDiv = document.createElement('div');
            cellDiv.className = 'cell';
            cellDiv.innerText = cell;
            matrixDiv.appendChild(cellDiv);
        });
    });
}

function botSelectFromOuterLayer(matrix) {
    const outerLayer = [
        ...matrix[0],
        ...matrix[matrix.length - 1],
        ...matrix.slice(1, -1).map(row => row[0]),
        ...matrix.slice(1, -1).map(row => row[row.length - 1])
    ];
    return outerLayer[Math.floor(Math.random() * outerLayer.length)];
}

function chooseRandomNumberInMatrix(matrix) {
    const flatMatrix = matrix.flat();
    return flatMatrix[Math.floor(Math.random() * flatMatrix.length)];
}

function findPath(matrix, botNumber, numberToFind) {
    const numRows = matrix.length;
    const numCols = matrix[0].length;
    const visited = Array.from({ length: numRows }, () => Array(numCols).fill(false));
    let visitedCount = 0;

    let startRow, startCol;
    outer: for (let row = 0; row < numRows; row++) {
        for (let col = 0; col < numCols; col++) {
            if (matrix[row][col] === botNumber) {
                startRow = row;
                startCol = col;
                break outer;
            }
        }
    }

    if (startRow === undefined || startCol === undefined) {
        console.log("Bot number not found in the matrix.");
        return null;
    }

    let currentRow = startRow, currentCol = startCol;
    const path = [matrix[currentRow][currentCol]];

    while (matrix[currentRow][currentCol] !== numberToFind) {
        visited[currentRow][currentCol] = true;
        visitedCount++;

        const adjacent = findAdjacent(matrix, currentRow, currentCol);
        let minDistance = Infinity;
        let nextRow = null, nextCol = null;

        for (const [r, c] of adjacent) {
            if (!visited[r][c]) {
                const distance = Math.abs(matrix[r][c] - numberToFind);
                if (distance < minDistance) {
                    minDistance = distance;
                    nextRow = r;
                    nextCol = c;
                }
            }
        }

        if (nextRow === null || nextCol === null) {
            console.log(`Number ${numberToFind} not found in the matrix reachable from bot number ${botNumber}.`);
            return null;
        }

        currentRow = nextRow;
        currentCol = nextCol;
        path.push(matrix[currentRow][currentCol]);
    }

    return path;
}

function findAdjacent(matrix, row, col) {
    const directions = [
        [0, 1], [0, -1], [1, 0], [-1, 0],
        [1, 1], [1, -1], [-1, 1], [-1, -1]
    ];
    const adjacent = [];

    for (const [dr, dc] of directions) {
        const newRow = row + dr;
        const newCol = col + dc;
        if (newRow >= 0 && newRow < matrix.length && newCol >= 0 && newCol < matrix[0].length) {
            adjacent.push([newRow, newCol]);
        }
    }

    return adjacent;
}

function highlightPath(matrix, path) {
    const cells = document.querySelectorAll('.cell');
    let cellIndex = 0;
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (path.includes(matrix[i][j])) {
                cells[cellIndex].classList.add('path');
            }
            cellIndex++;
        }
    }
}
