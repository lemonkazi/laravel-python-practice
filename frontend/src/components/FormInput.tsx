interface Form {
  labelFor: string;
  label: string;
  type?: string;
  name: string;
  placeholder: string;
}

export function FormInput({
  labelFor,
  label,
  type = "text",
  name,
  placeholder,
}: Form) {
  return (
    <div className="flex flex-col gap-2 mb-4">
      <label htmlFor={labelFor} className="text-base text-white">
        {label}
      </label>
      <input
        type={type}
        name={name}
        id={labelFor}
        placeholder={placeholder}
        className="px-4 py-2 rounded-lg bg-gray-700 text-white border border-gray-600 focus:outline-none focus:ring-2 focus:ring-green-500"
        required={true}
      />
    </div>
  );
}
