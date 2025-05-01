document.addEventListener("DOMContentLoaded", () => {
    const forgotPasswordForm = document.getElementById("forgot-password-form")
  
    // Form validation
    if (forgotPasswordForm) {
      forgotPasswordForm.addEventListener("submit", (e) => {
        const email = document.getElementById("email").value
        let isValid = true
  
        // Simple validation
        if (!email || !isValidEmail(email)) {
          isValid = false
          showError("email", "Please enter a valid email address")
        } else {
          removeError("email")
        }
  
        if (!isValid) {
          e.preventDefault()
        }
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
  