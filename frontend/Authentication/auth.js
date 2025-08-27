document.addEventListener('DOMContentLoaded', function() {
    // Toggle between login and register forms
    const loginToggle = document.getElementById('login-toggle');
    const registerToggle = document.getElementById('register-toggle');
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    
    loginToggle.addEventListener('click', function() {
        loginToggle.classList.add('active');
        registerToggle.classList.remove('active');
        loginForm.classList.add('active');
        registerForm.classList.remove('active');
    });
    
    registerToggle.addEventListener('click', function() {
        registerToggle.classList.add('active');
        loginToggle.classList.remove('active');
        registerForm.classList.add('active');
        loginForm.classList.remove('active');
    });
    
    // Form submission
    loginForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const email = document.getElementById('loginEmail').value;
        const password = document.getElementById('loginPassword').value;
        
        try {
            const response = await fetch('/api/auth/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            const data = await response.json();
            if (response.ok) {
                localStorage.setItem('token', data.token);
                window.location.href = '../Dashboard_and_Cart/dashboard.html';
            } else {
                showMessage(data.message, 'error');
            }
        } catch (error) {
            showMessage('An error occurred. Please try again.', 'error');
        }
    });
    
    registerForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const name = document.getElementById('registerName').value;
        const email = document.getElementById('registerEmail').value;
        const password = document.getElementById('registerPassword').value;
        const confirmPassword = document.getElementById('registerConfirmPassword').value;
        
        if (password !== confirmPassword) {
            showMessage('Passwords do not match!', 'error');
            return;
        }
        
        try {
            const response = await fetch('/api/auth/register', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name, email, password })
            });

            const data = await response.json();
            if (response.ok) {
                showMessage('Registration successful! Please login.', 'success');
                registerForm.reset();
                loginToggle.click();
            } else {
                showMessage(data.message, 'error');
            }
        } catch (error) {
            showMessage('An error occurred. Please try again.', 'error');
        }
    });
    
    function showMessage(message, type) {
            const toastEl = document.getElementById('liveToast');
    const toastBody = document.getElementById('toast-message');

    toastBody.textContent = message;

    // Reset classes
    toastEl.classList.remove('bg-success', 'bg-danger');

    if (type === 'success') {
        toastEl.classList.add('bg-success');
    } else {
        toastEl.classList.add('bg-danger');
    }

    const toast = new bootstrap.Toast(toastEl);
    toast.show();

    }
});