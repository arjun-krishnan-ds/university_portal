// Cards fade-up on scroll
const cards = document.querySelectorAll('.card');
const footer = document.querySelector('footer');

const revealOnScroll = () => {
    const windowHeight = window.innerHeight;

    cards.forEach(card => {
        const cardTop = card.getBoundingClientRect().top;
        if(cardTop < windowHeight - 100) {
            card.classList.add('show');
        }
    });

    if(footer.getBoundingClientRect().top < windowHeight - 50){
        footer.classList.add('show');
    }
}
const slides = document.querySelectorAll(".slide");
let currentSlide = 0;

setInterval(() => {
    slides[currentSlide].classList.remove("active");
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add("active");
}, 5000);

// Counter Animation
const counters = document.querySelectorAll('.counter');

counters.forEach(counter => {
    const updateCounter = () => {
        const target = +counter.getAttribute('data-target');
        const count = +counter.innerText;
        const speed = 200; // lower = faster
        const increment = target / speed;

        if(count < target){
            counter.innerText = Math.ceil(count + increment);
            setTimeout(updateCounter, 20);
        } else {
            counter.innerText = target;
        }
    }
    updateCounter();
});



