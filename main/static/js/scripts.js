
window.addEventListener('DOMContentLoaded', event => {

    /**
    * Back to top button
    */
    let backtotop = document.querySelector('.back-to-top');

    if (backtotop) {
      const toggleBacktotop = () => {
        if (window.scrollY > 100) {
          backtotop.classList.add('active');
        } else {
          backtotop.classList.remove('active');
        }
      };

      window.addEventListener('load', toggleBacktotop);
      window.addEventListener('scroll', toggleBacktotop);
    }

    let backtotop2 = document.querySelector('.back-to-top2');

    if (backtotop2) {
      const toggleBacktotop2 = () => {
        if (window.scrollY > 100) {
          backtotop2.classList.add('active');
        } else {
          backtotop2.classList.remove('active');
        }
      };

      window.addEventListener('load', toggleBacktotop2);
      window.addEventListener('scroll', toggleBacktotop2);
    }

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    //  Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});
