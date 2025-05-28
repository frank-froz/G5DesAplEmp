const variantClassMap = {
  primary: "button--primary",
  "outline-primary": "button--outline-primary",
  secondary: "button--secondary",
  link: "button--link",
};

const Button = ({
  text,
  variant = "",
  disabled = false,
  className = "",
  type = "button",
  onClick,
  ariaLabel,
}) => {
  const variantClass = variantClassMap[variant] || "";
  const classes = `button ${variantClass} ${className}`.trim();

  return (
    <button
      type={type}
      disabled={disabled}
      className={classes}
      onClick={onClick}
      aria-label={ariaLabel || text}
    >
      {text}
    </button>
  );
};

export default Button;