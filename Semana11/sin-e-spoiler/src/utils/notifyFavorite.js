import { toast } from "react-toastify";

export function notifyFavorite(movie, added) {
  const message = added
    ? `❤️ "${movie.title}" added to favorites!`
    : `💔 "${movie.title}" removed from favorites`;
  toast[added ? "success" : "info"](message, {
    position: "top-right",
    autoClose: 3000,
    pauseOnHover: true,
    hideProgressBar: false
  });
}
