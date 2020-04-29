let popular_movies = null;
let user1priority1 = null;
let user1priority2 = null;
let user1priority3 = null;

// Apurba's API Key - 343555bb
// Ranajoy's API Key - 78377031
let apiKey = "78377031";


// let user1priority3 = `
// {
//   "user_id": 1,
//   "priority": 3,
//   "movies": [
//   {
//   "movie_id": 131237,
//   "imdb_id": "tt1595366",
//   "tmdb_id": "1595366",
//   "title": "What Men Talk About (2010)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 134109,
//   "imdb_id": "tt1217565",
//   "tmdb_id": "1217565",
//   "title": "Radio Day (2008)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 134847,
//   "imdb_id": "tt1924273",
//   "tmdb_id": "1924273",
//   "title": "Ghost Graduation (2012)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 136445,
//   "imdb_id": "tt0246641",
//   "tmdb_id": "246641",
//   "title": "George Carlin: Back in Town (1996)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 136447,
//   "imdb_id": "tt0246645",
//   "tmdb_id": "246645",
//   "title": "George Carlin: You Are All Diseased (1999)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 136469,
//   "imdb_id": "tt0218388",
//   "tmdb_id": "218388",
//   "title": "Larry David: Curb Your Enthusiasm (1999)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 140265,
//   "imdb_id": "tt0246643",
//   "tmdb_id": "246643",
//   "title": "George Carlin: Jammin' in New York (1992)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 142020,
//   "imdb_id": "tt0062083",
//   "tmdb_id": "62083",
//   "title": "Oscar (1967)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 145994,
//   "imdb_id": "tt0216755",
//   "tmdb_id": "216755",
//   "title": "Formula of Love (1984)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 158398,
//   "imdb_id": "tt0102083",
//   "tmdb_id": "102083",
//   "title": "World of Glory (1991)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 162344,
//   "imdb_id": "tt4970632",
//   "tmdb_id": "4970632",
//   "title": "Tom Segura: Mostly Stories (2016)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 173963,
//   "imdb_id": "tt0809951",
//   "tmdb_id": "809951",
//   "title": "Empties (2007)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 174551,
//   "imdb_id": "tt0862766",
//   "tmdb_id": "862766",
//   "title": "Obsession (1965)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 3302,
//   "imdb_id": "tt0159272",
//   "tmdb_id": "159272",
//   "title": "Beautiful People (1999)",
//   "genres": "Comedy"
//   },
//   {
//   "movie_id": 2295,
//   "imdb_id": "tt0120823",
//   "tmdb_id": "120823",
//   "title": "Impostors, The (1998)",
//   "genres": "Comedy"
//   }
//   ],
//   "hasMovies": true,
//   "movieCount": 15
//   }
// `;









$(document).ready(() => {
  if (sessionStorage.getItem('userId')) {
    document.getElementById("user-display").innerHTML = sessionStorage.getItem('userId');
  } else {
    document.getElementById("user-display").innerHTML = "No one";
  }
  $('#searchForm').on('submit', (e) => {
    let searchText = $('#searchText').val();
    //getMovies(searchText);
    getMoviesStud(searchText);
    e.preventDefault();
  });

  // let viewBtn = document.getElementById("view-button");

  // viewBtn.addEventListener("click", function(){
  $('#view-button').on('click', (e) => {
    let userTxt = document.getElementById("user-id-text");
    // alert("written something");
    console.log("userTxt.value = " + userTxt.value);
    if (userTxt.value.length === 0) {
      alert("Please enter an user id");
    } else {
      axios.get('http://127.0.0.1:5000/check_user?uid=' + userTxt.value)
        .then((response) => {
          // alert("got a response");
          console.log(response);
          let obj = response.data;
          // let uids = obj.user_ids;
          // console.log(uids);
          let userFound = obj.exist;
          // for(let i = 0; i < uids.length; i++){
          //   if (userTxt.value == uids[i]) {
          //     userFound = true;
          //     break;
          //     //console.log('valid user'); not printing
          //     // userSelected(userTxt);
          //   }
          // }
          // alert("userFound = " + userFound);
          if (userFound) {
            // console.log('valid user'); not printing
            userSelected(userTxt.value);
            // alert("User found");
          } else {
            alert('User does not exist');
          }
        })
        .catch((err) => {
          console.log(err);
        });
      // TODO (done above): Check if the user exists by calling the API and checking 
      // to see if the entered user id is valid
      // If it is valid, call the userSelected() function with the user id
      // If it is invalid, display an alert box with suitable message
    }
    e.preventDefault();
  });
})

// OKAY! KORE FELO! DO IT!

// function getMovies(searchText){
//   axios.get('http://www.omdbapi.com?apikey=343555bb&s='+searchText)
//     .then((response) => {
//       console.log(response);
//       let movies = response.data.Search;
//       let output = '';
//       $.each(movies, (index, movie) => {
//         output += `
//           <div class="col-md-3">
//             <div class="well text-center">
//               <img src="${movie.Poster}">
//               <h5>${movie.Title}</h5>
//               <a onclick="movieSelected('${movie.imdbID}')" class="btn btn-primary" href="#">Movie Details</a>
//             </div>
//           </div>
//         `;
//       });

//       $('#movies').html(output);
//     })
//     .catch((err) => {
//       console.log(err);
//     }); 
// }


function getMoviesStud(searchText) {
  // let obj = null;
  console.log("searchText = " + searchText);
  // TODO: Call our own API to get the next JSON data
  if (searchText.length != 0) {
    axios.get('http://127.0.0.1:5000/search?title=' + searchText)
      .then((response) => {
        console.log("haha")
        console.log(response);
        let obj = response.data;
        let movieCount = obj.movieCount;
        let movieArr = obj.movies;
        // Apurba's API Key - 343555bb
        // Ranajoy's API Key - 78377031
        let poster_link = "http://img.omdbapi.com/?apikey=" + apiKey + "&i=";
        let output = '';
        for (var i = 0; i < movieCount; i++) {
          let arr_element = movieArr[i];
          let imdb_id = arr_element.imdb_id;
          output += `
            <div class="col-md-3">
              <div class="well text-center">
                <img src="${poster_link + imdb_id}">
                <h5>${arr_element.title}</h5>
                <a onclick="movieSelected('${imdb_id}', '${arr_element.movie_id}', '${arr_element.genres}')" class="btn btn-primary" href="#">Movie Details</a>
              </div>
            </div>
          `;
        }
        // //console.log(output);
        document.getElementById('movies').innerHTML = output;
      })
      .catch((err) => {
        console.log(err);
      });
  } else {
    document.getElementById('movies').innerHTML = "";
  }
  // let obj = JSON.parse(search_data);
  //console.log(obj);
}

function userSelected(userId) {
  // TODO: Store the userId in sessionStorage and change the window.location
  // to "user.html"
  sessionStorage.setItem('userId', userId);
  window.location = 'user.html';
  return false;
}

function movieSelected(imdb_id, movie_id, genres) {
  // TODO: Add the movie_id from database (not the imdb id)
  // to the sessionStorage
  console.log("movie_id: " + movie_id);
  console.log("imdb_id: " + imdb_id);
  sessionStorage.setItem('imdb_id', imdb_id);
  sessionStorage.setItem('movie_id', movie_id);
  sessionStorage.setItem('genres', genres);
  window.location = 'movie.html';
  return false;
}

function openModal() {
  $("#myModal").modal('show')
}

function ratings() {
  var radios = document.getElementsByTagName('input');
  var value;
  for (var i = 0; i < radios.length; i++) {
    if (radios[i].type === 'radio' && radios[i].checked) {
      // get value, set checked flag or do whatever you need to
      value = (radios[i].value) / 2;
      if (value === 0)
        value = null;
      // console.log(value);
      // console.log(value);
      // if (value != 0)
      //   console.log(value);
      // else
      //   console.log(null);
    }
  }
  // TODO: Make an API call to save user_id movie_id and the rating
  // User_id, movie_id -> sessionStorage
  // rating -> value
  // Display the success or failure message as 
  let user_id = sessionStorage.getItem('userId');
  let movie_id = sessionStorage.getItem('movie_id');
  let rating = value;
  // const axios = require('axios')
  axios.get('http://127.0.0.1:5000/add_user_rating?uid=' + user_id + '&mid=' + movie_id + '&rating=' + rating)
    .then((response) => {
      let status = response.data.success;
      if (status) {
        let w = '';
        w = `
        <div class="alert alert-dismissible alert-success">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        <strong>Successfully added your rating!</strong>
        </div>
        `;
        document.getElementById("success").innerHTML = w;
      } else {
        let w = '';
        w = `
        <div class="alert alert-dismissible alert-danger">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        <strong>Oh snap! Unable to add rating :(</strong>
        </div>
        `;
        document.getElementById("failure").innerHTML = w;
      }
    }, (error) => {
      console.log(error);
    });
  // axios.post('http://127.0.0.1:5000/add_user_rating',
  //    {"uid": user_id, "mid": movie_id, "rating": rating}
  //   )
  // .then((response) => {
  //   let status = response.data.success;
  //   if (status) {
  //     let w = '';
  //     w = `
  //       <div class="alert alert-dismissible alert-success">
  //       <button type="button" class="close" data-dismiss="alert">&times;</button>
  //       <strong>Successfully added your rating!</strong>
  //       </div>
  //       `;
  //     document.getElementById("success").innerHTML = w;
  //   }
  //   else {
  //     let w = '';
  //     w = `
  //       <div class="alert alert-dismissible alert-danger">
  //       <button type="button" class="close" data-dismiss="alert">&times;</button>
  //       <strong>Oh snap! Unable to add rating :(</strong>
  //       </div>
  //       `;
  //     document.getElementById("failure").innerHTML = w;
  //   }
  // }).catch((err) => {
  //   console.log(err);
  // }); 
}























function sec43() {
  // let obj = JSON.parse(user1priority3);
  obj = user1priority3;
  let movieCount = obj.movieCount;
  let movieArr = obj.movies;
  let item_link = "http://img.omdbapi.com/?apikey=" + apiKey + "&i=";

  let output = '<a href="#section42" class="arrow__btn" onclick="sec42()">‹</a>';
  for (var i = 10; i < 15; i++) {
    let arr_element = movieArr[i];
    let imdb_id = arr_element.imdb_id;
    let mov_title = arr_element.title;
    output += `
        <div class="item textWithBlurredBg">
          <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}', '${arr_element.movie_id}', '${arr_element.genres}')">
          <h5>${mov_title}</h5>
        </div>
    `;
  }
  output += '<a href="#section41" class="arrow__btn" onclick="populatePriority3()">›</a>'
  document.getElementById('section43').innerHTML = output;
}

function sec42() {
  // let obj = JSON.parse(user1priority3);
  obj = user1priority3;
  let movieCount = obj.movieCount;
  let movieArr = obj.movies;
  let item_link = "http://img.omdbapi.com/?apikey=" + apiKey + "&i=";

  let output = '<a href="#section41" class="arrow__btn" onclick="populatePriority3()">‹</a>';
  for (var i = 5; i < 10; i++) {
    let arr_element = movieArr[i];
    let imdb_id = arr_element.imdb_id;
    let mov_title = arr_element.title;
    output += `
        <div class="item textWithBlurredBg">
          <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}', '${arr_element.movie_id}', '${arr_element.genres}')">
          <h5>${mov_title}</h5>
        </div>
    `;
  }
  output += '<a href="#section43" class="arrow__btn" onclick="sec43()">›</a>'
  document.getElementById('section42').innerHTML = output;
}


function populatePriority3() {
  // TODO: Instead of the hardcoded value, fetch the recommendations from 
  // the API, use the user id from the sessionStorage
  // let userId = sessionStorage.getItem('userId');
  // let obj = JSON.parse(user1priority3);
  obj = user1priority3;
  let movieCount = obj.movieCount;
  let movieArr = obj.movies;
  let item_link = "http://img.omdbapi.com/?apikey=" + apiKey + "&i=";

  let output = '<a href="#section43" class="arrow__btn" onclick="sec43()">‹</a>';
  for (var i = 0; i < 5; i++) {
    let arr_element = movieArr[i];
    let imdb_id = arr_element.imdb_id;
    let mov_title = arr_element.title;
    output += `
        <div class="item textWithBlurredBg">
          <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}', '${arr_element.movie_id}', '${arr_element.genres}')">
          <h5>${mov_title}</h5>
        </div>
    `;
  }
  output += '<a href="#section42" class="arrow__btn" onclick="sec42()">›</a>'
  document.getElementById('section41').innerHTML = output;
}

























function sec33() {
  // let obj = JSON.parse(user1priority2);
  let obj = user1priority2;
  let movieCount = obj.movieCount;
  let movieArr = obj.movies;
  let item_link = "http://img.omdbapi.com/?apikey=" + apiKey + "&i=";

  let output = '<a href="#section32" class="arrow__btn" onclick="sec32()">‹</a>';
  for (var i = 10; i < 15; i++) {
    let arr_element = movieArr[i];
    let imdb_id = arr_element.imdb_id;
    let mov_title = arr_element.title;
    output += `
        <div class="item textWithBlurredBg">
          <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}', '${arr_element.movie_id}', '${arr_element.genres}')">
          <h5>${mov_title}</h5>
        </div>
    `;
  }
  output += '<a href="#section31" class="arrow__btn" onclick="populatePriority2()">›</a>'
  document.getElementById('section33').innerHTML = output;
}

function sec32() {
  // let obj = JSON.parse(user1priority2);
  let obj = user1priority2;
  let movieCount = obj.movieCount;
  let movieArr = obj.movies;
  let item_link = "http://img.omdbapi.com/?apikey=" + apiKey + "&i=";

  let output = '<a href="#section31" class="arrow__btn" onclick="populatePriority2()">‹</a>';
  for (var i = 5; i < 10; i++) {
    let arr_element = movieArr[i];
    let imdb_id = arr_element.imdb_id;
    let mov_title = arr_element.title;
    output += `
        <div class="item textWithBlurredBg">
          <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}', '${arr_element.movie_id}', '${arr_element.genres}')">
          <h5>${mov_title}</h5>
        </div>
    `;
  }
  output += '<a href="#section33" class="arrow__btn" onclick="sec33()">›</a>'
  document.getElementById('section32').innerHTML = output;
}


function populatePriority2() {
  // TODO: Instead of the hardcoded value, fetch the recommendations from 
  // the API, use the user id from the sessionStorage
  // let userId = sessionStorage.getItem('userId');
  // let obj = JSON.parse(user1priority2);
  obj = user1priority2;
  let movieCount = obj.movieCount;
  let movieArr = obj.movies;
  let item_link = "http://img.omdbapi.com/?apikey=" + apiKey + "&i=";

  let output = '<a href="#section33" class="arrow__btn" onclick="sec33()">‹</a>';
  for (var i = 0; i < 5; i++) {
    let arr_element = movieArr[i];
    let imdb_id = arr_element.imdb_id;
    let mov_title = arr_element.title;
    output += `
        <div class="item textWithBlurredBg">
          <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}', '${arr_element.movie_id}', '${arr_element.genres}')">
          <h5>${mov_title}</h5>
        </div>
    `;
  }
  output += '<a href="#section32" class="arrow__btn" onclick="sec32()">›</a>'
  document.getElementById('section31').innerHTML = output;
}


































function sec23() {
  // let obj = JSON.parse(user1priority1);
  let obj = user1priority1;
  let movieCount = obj.movieCount;
  let movieArr = obj.movies;
  let item_link = "http://img.omdbapi.com/?apikey=" + apiKey + "&i=";

  let output = '<a href="#section22" class="arrow__btn" onclick="sec22()">‹</a>';
  for (var i = 10; i < 15; i++) {
    let arr_element = movieArr[i];
    let imdb_id = arr_element.imdb_id;
    let mov_title = arr_element.title;
    output += `
        <div class="item textWithBlurredBg">
          <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}', '${arr_element.movie_id}', '${arr_element.genres}')">
          <h5>${mov_title}</h5>
        </div>
    `;
  }
  output += '<a href="#section21" class="arrow__btn" onclick="populatePriority1()">›</a>'
  document.getElementById('section23').innerHTML = output;
}

function sec22() {
  // let obj = JSON.parse(user1priority1);
  let obj = user1priority1;
  let movieCount = obj.movieCount;
  let movieArr = obj.movies;
  let item_link = "http://img.omdbapi.com/?apikey=" + apiKey + "&i=";

  let output = '<a href="#section21" class="arrow__btn" onclick="populatePriority1()">‹</a>';
  for (var i = 5; i < 10; i++) {
    let arr_element = movieArr[i];
    let imdb_id = arr_element.imdb_id;
    let mov_title = arr_element.title;
    output += `
        <div class="item textWithBlurredBg">
          <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}', '${arr_element.movie_id}', '${arr_element.genres}')">
          <h5>${mov_title}</h5>
        </div>
    `;
  }
  output += '<a href="#section23" class="arrow__btn" onclick="sec23()">›</a>'
  document.getElementById('section22').innerHTML = output;
}


function populatePriority1() {
  // TODO: Instead of the hardcoded value, fetch the recommendations from 
  // the API, use the user id from the sessionStorage
  // let userId = sessionStorage.getItem('userId');
  // let obj = JSON.parse(user1priority1);
  let obj = user1priority1;
  let movieCount = obj.movieCount;
  let movieArr = obj.movies;
  let item_link = "http://img.omdbapi.com/?apikey=" + apiKey + "&i=";

  let output = '<a href="#section23" class="arrow__btn" onclick="sec23()">‹</a>';
  for (var i = 0; i < 5; i++) {
    let arr_element = movieArr[i];
    let imdb_id = arr_element.imdb_id;
    let mov_title = arr_element.title;
    output += `
        <div class="item textWithBlurredBg">
          <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}', '${arr_element.movie_id}', '${arr_element.genres}')">
          <h5>${mov_title}</h5>
        </div>
    `;
  }
  output += '<a href="#section22" class="arrow__btn" onclick="sec22()">›</a>'
  document.getElementById('section21').innerHTML = output;
}





































function sec13() {
  // let obj = JSON.parse(popular_movies_hard)
  let obj = popular_movies;
  let movieArr = obj.movies;
  let item_link = "http://img.omdbapi.com/?apikey= " + apiKey + "&i=";

  let output = '<a href="#section12" class="arrow__btn" onclick="sec12()">‹</a>';
  for (var i = 10; i < 15; i++) {
    let arr_element = movieArr[i];
    let imdb_id = arr_element.imdb_id;
    let mov_title = arr_element.title;
    output += `
        <div class="item textWithBlurredBg">
          <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}', '${arr_element.movie_id}', '${arr_element.genres}')">
          <h5>${mov_title}</h5>
        </div>
    `;
  }
  output += '<a href="#section11" class="arrow__btn" onclick="populateCarousel()">›</a>'
  document.getElementById('section13').innerHTML = output;
  // let obj = JSON.parse(popular_movies);
  // let movieCount = obj.movieCount;
  // let movieArr = obj.movies;
  // let item_link = "http://img.omdbapi.com/?apikey=343555bb&i=";

  // let output = '<a href="#section11" class="arrow__btn" onclick="sec12()">‹</a>';
  // for(var i = 10; i < 15; i++){
  //   let arr_element = movieArr[i];
  //   let imdb_id = arr_element.imdb_id;
  //   let mov_title = arr_element.title;
  //   output += `
  //       <div class="item textWithBlurredBg">
  //         <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}')">
  //         <h5>${mov_title}</h5>
  //       </div>
  //   `;
  // }
  // output += '<a href="#section11" class="arrow__btn" onclick="sec13()">›</a>'
  // document.getElementById('section13').innerHTML = output;
}

function sec12() {
  // let obj = JSON.parse(popular_movies_hard)
  let obj = popular_movies;
  let movieArr = obj.movies;
  let item_link = "http://img.omdbapi.com/?apikey=" + apiKey + "&i=";

  let output = '<a href="#section11" class="arrow__btn" onclick="populateCarousel()">‹</a>';
  for (var i = 5; i < 10; i++) {
    let arr_element = movieArr[i];
    let imdb_id = arr_element.imdb_id;
    let mov_title = arr_element.title;
    output += `
        <div class="item textWithBlurredBg">
          <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}', '${arr_element.movie_id}', '${arr_element.genres}')">
          <h5>${mov_title}</h5>
        </div>
    `;
  }
  output += '<a href="#section13" class="arrow__btn" onclick="sec13()">›</a>'
  document.getElementById('section12').innerHTML = output;


  // let obj = JSON.parse(popular_movies);
  // let movieCount = obj.movieCount;
  // let movieArr = obj.movies;
  // let item_link = "http://img.omdbapi.com/?apikey=343555bb&i=";

  // let output = '<a href="#section11" class="arrow__btn" onclick="populateCarousel()">‹</a>';
  // for(var i = 5; i < 10; i++){
  //   let arr_element = movieArr[i];
  //   let imdb_id = arr_element.imdb_id;
  //   let mov_title = arr_element.title;
  //   output += `
  //       <div class="item textWithBlurredBg">
  //         <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}')">
  //         <h5>${mov_title}</h5>
  //       </div>
  //   `;
  // }
  // output += '<a href="#section13" class="arrow__btn" onclick="sec13()">›</a>'
  // document.getElementById('section12').innerHTML = output;
}


function populateCarousel() {
  // TODO: Instead of the hardcoded value, fetch the recommendations from 
  // the API, use the user id from the sessionStorage
  // let userId = sessionStorage.getItem('userId');

  // let obj = JSON.parse(popular_movies_hard);
  let obj = popular_movies;
  let movieCount = obj.movieCount;
  let movieArr = obj.movies;
  let item_link = "http://img.omdbapi.com/?apikey=" + apiKey + "&i=";

  let output = '<a href="#section13" class="arrow__btn" onclick="sec13()">‹</a>';
  for (var i = 0; i < 5; i++) {
    let arr_element = movieArr[i];
    let imdb_id = arr_element.imdb_id;
    let mov_title = arr_element.title;
    output += `
          <div class="item textWithBlurredBg">
            <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}', '${arr_element.movie_id}', '${arr_element.genres}')">
            <h5>${mov_title}</h5>
          </div>
      `;
  }
  output += '<a href="#section12" class="arrow__btn" onclick="sec12()">›</a>'
  document.getElementById('section11').innerHTML = output;
}

function renderHTML() {
  let userId = sessionStorage.getItem('userId');

  let is_generating_recommendation = 0;
  // Popular movies
  axios.get('http://127.0.0.1:5000/get_popular_movies?uid=' + userId)
    .then((response) => {
      let myData = response.data;
      // TEST CODE BELOW
      //myData.hasMovies = false;
      console.log("Popular")
      console.log(myData)
      if (myData.hasMovies) {
        popular_movies = myData;
        populateCarousel();
      } else {
        document.getElementById("popular-heading").style = "display: none;";
        // TODO (done): Add a blue messages stating "Popular movies not found"
        let w = '';
        w = `
          <div class="alert alert-dismissible alert-primary">
          <button type="button" class="close" data-dismiss="alert">&times;</button>
          <strong>Popular Movies not found!</strong>
          </div> 
          `;
        document.getElementById("popular-not-found").innerHTML = w;
      }
    })
    .catch((err) => {
      console.log(err);
    });
  // Priority 1
  axios.get('http://127.0.0.1:5000/get_movies_by_priority?uid=' + userId + '&pid=1')
    .then((response) => {
      let myData1 = response.data;
      console.log("Priority 1")
      console.log(myData1)
      if (myData1.is_generating_recommendation) {
        is_generating_recommendation = 1;
        let w = '';
        w = `
          <div class="alert alert-dismissible alert-warning">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            <h4 class="alert-heading">Warning!</h4>
            <p class="mb-0" style="font-size: 24px;">
              Please wait, generating your recommendations
            </p>
          </div>
          `;
        document.getElementById('generating-recommendation').innerHTML = w;
      }
      //TEST
      // myData1.hasMovies = false;
      console.log("myData1.hasMovies " + myData1.hasMovies);
      if (myData1.hasMovies) {
        user1priority1 = myData1;
        populatePriority1();
        // console.log(myData);
        // popular_movies = myData;
        // populateCarousel();
      } else {
        console.log("Priority 1 Movies Not found");
        document.getElementById("priority1-heading").style = "display: none;";
        let p1 = '';
        p1 = `
            <div class="alert alert-dismissible alert-primary">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            <strong>Priority-1 Movies not found!</strong>
            </div> 
            `;
        document.getElementById("priority1-not-found").innerHTML = p1;
      }
    })
    .catch((err) => {
      console.log(err);
    });
  // Priority 2
  axios.get('http://127.0.0.1:5000/get_movies_by_priority?uid=' + userId + '&pid=2')
    .then((response) => {
      let myData2 = response.data;
      console.log("Priority 2")
      console.log(myData2)
      //TEST
      // myData2.hasMovies = false;
      console.log("myData2.hasMovies " + myData2.hasMovies);
      if (myData2.hasMovies) {
        user1priority2 = myData2;
        populatePriority2();
        // console.log(myData);
        // popular_movies = myData;
        // populateCarousel();
      } else {
        console.log("Priority 2 Movies Not found");
        document.getElementById("priority2-heading").style = "display: none;";
        let p2 = '';
        p2 = `
            <div class="alert alert-dismissible alert-primary">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            <strong>Priority-2 Movies not found!</strong>
            </div> 
            `;
        document.getElementById("priority2-not-found").innerHTML = p2;
      }
    })
    .catch((err) => {
      console.log(err);
    });
  // Priority 3
  axios.get('http://127.0.0.1:5000/get_movies_by_priority?uid=' + userId + '&pid=3')
    .then((response) => {
      let myData3 = response.data;
      console.log("Priority 3")
      console.log(myData3)
      //TEST
      // myData3.hasMovies = false;
      console.log("myData3.hasMovies " + myData3.hasMovies);
      if (myData3.hasMovies) {
        user1priority3 = myData3;
        populatePriority3();
        // console.log(myData);
        // popular_movies = myData;
        // populateCarousel();
      } else {
        console.log("Priority 3 Movies Not found");
        document.getElementById("priority3-heading").style = "display: none;";
        let p3 = '';
        p3 = `
            <div class="alert alert-dismissible alert-primary">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            <strong>Priority-3 Movies not found!</strong>
            </div> 
            `;
        document.getElementById("priority3-not-found").innerHTML = p3;
      }
    })
    .catch((err) => {
      console.log(err);
    });
  // TEST CODE BELOW
  // is_generating_recommendation = 3;

}



// let output = '<a href="#section11" class="arrow__btn">‹</a>';
// for(var i = 5; i < 10; i++){
//   let arr_element = movieArr[i];
//   let imdb_id = arr_element.imdb_id;
//   let mov_title = arr_element.title;
//   output += `
//       <div class="item textWithBlurredBg">
//         <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}')">
//         <h5>${mov_title}</h5>
//       </div>
//   `;
// }
// output += '<a href="#section13" class="arrow__btn">›</a>'
// document.getElementById('section12').innerHTML = output;


// let output = '<a href="#section12" class="arrow__btn">‹</a>';
// for(var i = 10; i < 15; i++){
//   let arr_element = movieArr[i];
//   let imdb_id = arr_element.imdb_id;
//   let mov_title = arr_element.title;
//   output += `
//       <div class="item textWithBlurredBg">
//         <img class="poster" src="${item_link + imdb_id}" onclick="movieSelected('${imdb_id}')">
//         <h5>${mov_title}</h5>
//       </div>
//   `;
// }
// output += '<a href="#section11" class="arrow__btn">›</a>'
// document.getElementById('section13').innerHTML = output;



function getMovie() {
  let imdbId = sessionStorage.getItem('imdb_id');
  let uid = sessionStorage.getItem('userId');
  let mid = sessionStorage.getItem('movie_id');
  let genres = sessionStorage.getItem('genres');
  let avg_rating = null;
  let user_rating = null;
  // axios.get('http://127.0.0.1:5000/get_average_rating?mid=' + movie_id)
  //   .then((response) => {
  //     console.log(response);
  //     avg_rating = response.data.average_rating;
  //     console.log('average_rating is: ' + avg_rating);
  //   })
  //   .catch((err) => {
  //     console.log(err);
  //   });
  // TODO: Get the average rating and user rating by calling the 
  // API, the userId will be available from the sessionStorage
  // Ranajoy's API Key - 78377031
  // Apurba's API Key - 343555bb
  axios.get('http://www.omdbapi.com?apikey=' + apiKey + '&i=' + imdbId)
    .then((response) => {
      console.log(response);
      let movie = response.data;
      axios.get('http://127.0.0.1:5000/get_average_rating?mid=' + mid)
        .then((response) => {
          console.log(response);
          avg_rating = response.data.average_rating;
          // console.log('average_rating is: ' + avg_rating);
          axios.get('http://127.0.0.1:5000/get_rating_by_user?uid=' + uid + '&mid=' + mid)
            .then((response) => {
              user_rating = response.data.rating;
              console.log('user_rating is: ' + user_rating);
              axios.get('http://127.0.0.1:5000/has_watched?uid=' + uid + '&mid=' + mid)
                .then((response) => {
                  console.log(response);
                  let hasWatched = response.data.has_watched;
                  let output = `
        <div class="row">
          <div class="col-md-4">
            <img src="${movie.Poster}" class="thumbnail">
          </div>
          <div class="col-md-8">
            <h2>${movie.Title}</h2>

            <!-- Necessary scripts to run modal -->

            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>

            <!-- Trigger modal using a button -->
            <button type="button" class="btn btn-success" onclick="openModal()">Watch</button>
            
            <!-- Modal goes below -->
            
            <div id="myModal" class="modal fade">
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title">Rate this movie</h5>
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="modal-body">
                  <p>Your rating matters!</p>
                  
                  <fieldset class="rate">
                      <input type="radio" id="rating10" name="rating" value="10" /><label for="rating10" title="5 stars"></label>
                      <input type="radio" id="rating9" name="rating" value="9" /><label class="half" for="rating9" title="4.5 stars"></label>
                      <input type="radio" id="rating8" name="rating" value="8" /><label for="rating8" title="4 stars"></label>
                      <input type="radio" id="rating7" name="rating" value="7" /><label class="half" for="rating7" title="3.5 stars"></label>
                      <input type="radio" id="rating6" name="rating" value="6" /><label for="rating6" title="3 stars"></label>
                      <input type="radio" id="rating5" name="rating" value="5" /><label class="half" for="rating5" title="2.5 stars"></label>
                      <input type="radio" id="rating4" name="rating" value="4" /><label for="rating4" title="2 stars"></label>
                      <input type="radio" id="rating3" name="rating" value="3" /><label class="half" for="rating3" title="1.5 stars"></label>
                      <input type="radio" id="rating2" name="rating" value="2" /><label for="rating2" title="1 star"></label>
                      <input type="radio" id="rating1" name="rating" value="1" /><label class="half" for="rating1" title="0.5 star"></label>
                      <input type="radio" id="rating0" name="rating" value="0" /><label for="rating0" title="No star"> |&nbsp;</label>
                  </fieldset>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-primary" data-dismiss="modal" onclick="ratings()">Submit</button>
                  <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                </div>
              </div>
            </div>
          </div>

          <!-- Modal over -->

            <ul class="list-group">
              <li class="list-group-item"><strong>Genre:</strong> ${genres}</li>
              <li class="list-group-item"><strong>Released:</strong> ${movie.Released}</li>
              <li class="list-group-item"><strong>Rated:</strong> ${movie.Rated}</li>
              <li class="list-group-item"><strong>IMDB Rating:</strong> ${movie.imdbRating}</li>
              <li class="list-group-item"><strong>Director:</strong> ${movie.Director}</li>
              <li class="list-group-item"><strong>Writer:</strong> ${movie.Writer}</li>
              <li class="list-group-item"><strong>Actors:</strong> ${movie.Actors}</li>
              <!-- TODO: Show the average rating -->
              <li class="list-group-item"><strong>Average Rating:</strong> ${avg_rating}</li>
              <!-- TODO: Show the users rating rating -->
              <li class="list-group-item"><strong>Users Rating:</strong> ${user_rating}</li>
              <li class="list-group-item"><strong>Has been seen by user:</strong> ${hasWatched ? 'Yes' : 'No'}</li>
            </ul>
          </div>
        </div>
        <div class="row">
          <div class="well">
            <h4>Plot</h4>
            ${movie.Plot}
            <hr>
            <a href="http://imdb.com/title/${movie.imdbID}" target="_blank" class="btn btn-primary">View on IMDB</a>
            &nbsp;
            &nbsp;
            &nbsp;
            &nbsp;
            &nbsp;
            &nbsp;
            &nbsp;
            &nbsp;
            &nbsp;
            &nbsp;
            &nbsp;
            &nbsp;
            <a href="index.html" class="btn btn-primary">Go Back To Search</a>
          </div>
        </div>
      `;
                  $('#movie').html(output);
                })
                .catch((err) => {
                  console.log(err);
                });
            })
            .catch((err) => {
              console.log(err);
            });

        })
        .catch((err) => {
          console.log(err);
        });


    })
    .catch((err) => {
      console.log(err);
    });
}