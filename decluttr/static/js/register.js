document.addEventListener("DOMContentLoaded", () => {
    const registerForm = document.getElementById("register-form")
    const githubRegisterBtn = document.getElementById("github-register")
  
    // Form validation
    if (registerForm) {
      registerForm.addEventListener("submit", (e) => {
        const firstName = document.getElementById("first-name").value
        const lastName = document.getElementById("last-name").value
        const email = document.getElementById("email").value
        const password = document.getElementById("password").value
        const confirmPassword = document.getElementById("confirm-password").value
        let isValid = true
  
        // Simple validation
        if (!firstName) {
          isValid = false
          showError("first-name", "Please enter your first name")
        } else {
          removeError("first-name")
        }
  
        if (!lastName) {
          isValid = false
          showError("last-name", "Please enter your last name")
        } else {
          removeError("last-name")
        }
  
        if (!email || !isValidEmail(email)) {
          isValid = false
          showError("email", "Please enter a valid email address")
        } else {
          removeError("email")
        }
  
        if (!password) {
          isValid = false
          showError("password", "Please enter a password")
        } else if (password.length < 8) {
          isValid = false
          showError("password", "Password must be at least 8 characters")
        } else {
          removeError("password")
        }
  
        if (password !== confirmPassword) {
          isValid = false
          showError("confirm-password", "Passwords do not match")
        } else {
          removeError("confirm-password")
        }
  
        if (!isValid) {
          e.preventDefault()
        }
      })
    }
  
    // GitHub registration
    if (githubRegisterBtn) {
      githubRegisterBtn.addEventListener("click", () => {
        // Redirect to GitHub OAuth route
        window.location.href = "/login/github"
      })
    }
  
    // Helper functions
    function isValidEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      return re.test(email)
    }
  
    function showError(inputId, message) {
      const input = document.getElementById(inputId)
      const errorDiv = document.createElement("div")
  
      // Remove any existing error
      removeError(inputId)
  
      errorDiv.className = "input-error"
      errorDiv.textContent = message
      errorDiv.style.color = "var(--error-color)"
      errorDiv.style.fontSize = "0.75rem"
      errorDiv.style.marginTop = "0.25rem"
  
      input.style.borderColor = "var(--error-color)"
      input.parentNode.appendChild(errorDiv)
    }
  
    function removeError(inputId) {
      const input = document.getElementById(inputId)
      const existingError = input.parentNode.querySelector(".input-error")
  
      if (existingError) {
        existingError.remove()
      }
  
      input.style.borderColor = ""
    }
  })
  