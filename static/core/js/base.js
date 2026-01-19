// ===============================
// Cards fade-up on scroll
// ===============================
const cards = document.querySelectorAll('.card');
const footer = document.querySelector('footer');

const revealOnScroll = () => {
    const windowHeight = window.innerHeight;

    if (cards.length) {
        cards.forEach(card => {
            const cardTop = card.getBoundingClientRect().top;
            if (cardTop < windowHeight - 100) {
                card.classList.add('show');
            }
        });
    }

    if (footer) {
        if (footer.getBoundingClientRect().top < windowHeight - 50) {
            footer.classList.add('show');
        }
    }
};

window.addEventListener('scroll', revealOnScroll);
revealOnScroll();


// ===============================
// Slider (SAFE)
// ===============================
const slides = document.querySelectorAll(".slide");
let currentSlide = 0;

if (slides.length > 0) {
    setInterval(() => {
        slides[currentSlide].classList.remove("active");
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add("active");
    }, 5000);
}


// ===============================
// Counter Animation (SAFE)
// ===============================
const counters = document.querySelectorAll('.counter');

if (counters.length) {
    counters.forEach(counter => {
        const updateCounter = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;
            const speed = 200;
            const increment = target / speed;

            if (count < target) {
                counter.innerText = Math.ceil(count + increment);
                setTimeout(updateCounter, 20);
            } else {
                counter.innerText = target;
            }
        };
        updateCounter();
    });
}
