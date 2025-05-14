// Movie data from TMDB API structure
export const nowPlayingMovies = {
  page: 1,
  results: [
    {
      adult: false,
      backdrop_path: "/cJvUJEEQ86LSjl4gFLkYpdCJC96.jpg",
      genre_ids: [10752, 28],
      id: 1241436,
      original_language: "en",
      original_title: "Warfare",
      overview: "A platoon of Navy SEALs embarks on a dangerous mission in Ramadi, Iraq, with the chaos and brotherhood of war retold through their memories of the event.",
      popularity: 485.3223,
      poster_path: "/j8tqBXwH2PxBPzbtO19BTF9Ukbf.jpg",
      release_date: "2025-04-09",
      title: "Warfare",
      video: false,
      vote_average: 7.14,
      vote_count: 265
    },
    {
      adult: false,
      backdrop_path: "/2Nti3gYAX513wvhp8IiLL6ZDyOm.jpg",
      genre_ids: [10751, 35, 12, 14],
      id: 950387,
      original_language: "en",
      original_title: "A Minecraft Movie",
      overview: "Four misfits find themselves struggling with ordinary problems when they are suddenly pulled through a mysterious portal into the Overworld: a bizarre, cubic wonderland that thrives on imagination.",
      popularity: 409.3111,
      poster_path: "/yFHHfHcUgGAxziP1C3lLt0q2T4s.jpg",
      release_date: "2025-03-31",
      title: "A Minecraft Movie",
      video: false,
      vote_average: 6.31,
      vote_count: 959
    },
    {
      adult: false,
      backdrop_path: "/jRvhP4AfFnJ03lCQhp1fie7XPSd.jpg",
      genre_ids: [28, 53],
      id: 977294,
      original_language: "en",
      original_title: "Tin Soldier",
      overview: "An ex-special forces operative seeks revenge against a cult leader who has corrupted his former comrades.",
      popularity: 383.402,
      poster_path: "/lFFDrFLXywFhy6khHes1LCFVMsL.jpg",
      release_date: "2025-05-22",
      title: "Tin Soldier",
      video: false,
      vote_average: 0.0,
      vote_count: 0
    }
  ],
  total_pages: 5,
  total_results: 100
};

// Helper function to get full image URL
export const getImageUrl = (path, size = "w342") => {
  return `https://image.tmdb.org/t/p/${size}${path}`;
};

// Map genre IDs to genre names
export const genres = {
  28: "Action",
  12: "Adventure",
  14: "Fantasy",
  35: "Comedy",
  53: "Thriller",
  10751: "Family",
  10752: "War"
};

// Convert TMDB data to our app structure
export const convertToAppFormat = (tmdbMovie) => {
  return {
    id: tmdbMovie.id,
    title: tmdbMovie.title,
    rating: tmdbMovie.vote_average / 2, // Convert from 10-point to 5-point scale
    genre: tmdbMovie.genre_ids.map(id => genres[id])[0] || "Unknown",
    duration: "120 min", // Placeholder since TMDB doesn't provide duration
    image: getImageUrl(tmdbMovie.poster_path),
    description: tmdbMovie.overview,
    showTimes: ["2:30 PM", "5:45 PM", "9:00 PM"], // Placeholder showtimes
    releaseDate: tmdbMovie.release_date
  };
};

// Get all movies in app format
export const getMovies = () => {
  return nowPlayingMovies.results.map(convertToAppFormat);
};

