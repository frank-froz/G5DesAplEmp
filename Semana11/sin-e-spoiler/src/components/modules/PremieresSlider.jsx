import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import LoadingSkeleton from "../widgets/LoadingSkeleton";

export default function PremieresSlider({ items, loading, onSelect }) {
  if (loading) {
    return <LoadingSkeleton count={4} height={200} />;
  }
  return (
    <Swiper
      slidesPerView={1}
      breakpoints={{ 640: { slidesPerView: 2 }, 1024: { slidesPerView: 4 } }}
      keyboard={{ enabled: true }}
      spaceBetween={16}
    >
      {items.map(movie => (
        <SwiperSlide key={movie.id}>
          <div
            tabIndex={0}
            className="p-relative"
            onClick={() => onSelect(movie)}
            onKeyDown={e => e.key === "Enter" && onSelect(movie)}
          >
            <img
              src={movie.image}
              alt={movie.title}
              className="card__image"
              loading="lazy"
            />
            <h3 className="title title--2xs c-primary">{movie.title}</h3>
          </div>
        </SwiperSlide>
      ))}
    </Swiper>
  );
}
