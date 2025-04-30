document.addEventListener('DOMContentLoaded', function() {
    // Add fade-in animation to posts
    const posts = document.querySelectorAll('.post');
    posts.forEach((post, index) => {
        post.style.opacity = '0';
        post.style.transition = 'opacity 0.5s ease';
        
        setTimeout(() => {
            post.style.opacity = '1';
        }, 100 * index);
    });
    
    // Add click event to categories dropdown (if exists)
    const categoryToggle = document.getElementById('category-toggle');
    const categoryDropdown = document.getElementById('category-dropdown');
    
    if (categoryToggle && categoryDropdown) {
        categoryToggle.addEventListener('click', function() {
            categoryDropdown.classList.toggle('active');
        });
    }
});