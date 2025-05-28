import { useForm } from "react-hook-form";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export default function SignupForm({ onSubmit }) {
  const { register, handleSubmit, formState: { errors, isSubmitting } } = useForm();

  const submit = async data => {
    await onSubmit(data);
    toast.success("📝 Signup successful!", { position: "top-right", autoClose: 3000 });
  };

  return (
    <form onSubmit={handleSubmit(submit)} className="form" aria-label="Signup form">
      <input
        {...register("name", { required: true })}
        placeholder="Name"
        className="form__input"
        aria-invalid={errors.name ? "true" : "false"}
      />
      {errors.name && <p role="alert">Name is required</p>}

      <input
        {...register("email", { required: true, pattern: /^\S+@\S+$/i })}
        placeholder="Email"
        className="form__input"
        aria-invalid={errors.email ? "true" : "false"}
      />
      {errors.email && <p role="alert">Enter a valid email</p>}

      <input
        type="password"
        {...register("password", { required: true, minLength: 6 })}
        placeholder="Password"
        className="form__input"
        aria-invalid={errors.password ? "true" : "false"}
      />
      {errors.password && <p role="alert">Password must be at least 6 characters</p>}

      <button type="submit" className="button button--primary" disabled={isSubmitting}>
        Sign Up
      </button>
    </form>
  );
}
