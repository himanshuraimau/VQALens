document.getElementById('imageInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const preview = document.getElementById('preview');
        preview.style.display = 'block';
        preview.src = URL.createObjectURL(file);
    }
});

async function askQuestion() {
    const imageInput = document.getElementById('imageInput');
    const questionInput = document.getElementById('question');
    const answerElement = document.getElementById('answer');
    const errorElement = document.getElementById('error');

    // Reset messages
    answerElement.textContent = '';
    errorElement.textContent = '';

    if (!imageInput.files[0]) {
        errorElement.textContent = 'Please select an image first.';
        return;
    }

    if (!questionInput.value.trim()) {
        errorElement.textContent = 'Please enter a question.';
        return;
    }

    const formData = new FormData();
    formData.append('image', imageInput.files[0]);
    formData.append('text', questionInput.value.trim());

    try {
        const response = await fetch('http://localhost:8000/ask', {
            method: 'POST',
            body: formData,
            headers: {
                'Accept': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        answerElement.textContent = `Answer: ${data.answer}`;
    } catch (error) {
        errorElement.textContent = `Error: ${error.message}`;
    }
}

// Add event listener for the form submission
document.getElementById('askForm').addEventListener('submit', function(event) {
    event.preventDefault();
    askQuestion();
});
