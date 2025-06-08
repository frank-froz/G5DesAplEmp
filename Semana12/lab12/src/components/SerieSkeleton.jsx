import Skeleton from "react-loading-skeleton";
import 'react-loading-skeleton/dist/skeleton.css';

function SerieSkeleton() {
  return (
    <div className="card">
      <Skeleton height={200} />
      <div className="card-body">
        <h5 className="card-title">
          <Skeleton width={`60%`} />
        </h5>
        <p className="card-text">
          <Skeleton width={`40%`} />
        </p>
      </div>
    </div>
  );
}

export default SerieSkeleton;
