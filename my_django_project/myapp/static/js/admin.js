function getTicketSales(movie_name) {
  const ticketDetailsUrl = `/admin_home/ticket-sold/${encodeURIComponent(movie_name)}/`;
  window.location.href = ticketDetailsUrl;
}


function searchMovies() {
    var input, filter, movies, movie, title, i;
    input = document.getElementById('searchInput');
    filter = input.value.toUpperCase();
    movies = document.querySelectorAll('.rmovies, .umovies');

    for (i = 0; i < movies.length; i++) {
      movie = movies[i];
      title = movie.textContent || movie.innerText;    
      if (title.toUpperCase().indexOf(filter) > -1) {
        movie.style.display = '';
      } else {
        movie.style.display = 'none';
      }
    }
  }
  document.getElementById('logoutbtn').addEventListener('click', function() {
    window.location.href = '/login/';
  });


