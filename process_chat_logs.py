import json
import sys

def process_chat_logs(input_file, output_file, user_role_name="User", unknown_role_name="Unknown"):
    try:
        with open(input_file, 'r', encoding='utf-8') as f_in:
            data = json.load(f_in)

        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write("# Chat Logs\n\n")

            if 'chunkedPrompt' in data and 'chunks' in data['chunkedPrompt']:
                chunks = data['chunkedPrompt']['chunks']

                for chunk in chunks:
                    role = chunk.get('role', 'unknown')
                    text = chunk.get('text', '').strip()

                    if role == 'user':
                        role_display = user_role_name
                    elif role == 'model':
                        role_display = "Assistant" # Consistent with previous examples
                    else:
                        role_display = unknown_role_name

                    if text:
                        f_out.write(f"**{role_display}:** {text}\n\n")
            else:
                f_out.write("Could not find conversation chunks in the expected format.\n")
                print("Warning: Could not find conversation chunks in the expected format.")

            # Handle pendingInputs (optional - we'll just ignore them)
            # if 'pendingInputs' in data:
            #     for pending in data['pendingInputs']:
            #         if pending.get('role') == 'user':
            #             f_out.write(f"**{user_role_name} (Incomplete):** {pending.get('text', '').strip()}\n\n")

            f_out.write("---\n")

        print(f"Successfully converted {input_file} to {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process_chat_logs.py <input_json_file> <output_md_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_chat_logs(input_file, output_file)  # Use default role names
    # OR, to customize role names:
    # process_chat_logs(input_file, output_file, user_role_name="Customer", unknown_role_name="Other")