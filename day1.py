import os
from dotenv import load_dotenv
from IPython.display import Markdown, display
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

# Check the key

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")

message = "Hello, GPT! This is my first ever message to you! Hi!"
messages = [
    {"role": "user", "content": message}
]

openai = OpenAI()

response = openai.chat.completions.create(model="gpt-5-nano", messages=messages)
print(response.choices[0].message.content)

system_prompt = """
You are an AI assistant for a university academic information system (SIAKAD).

Your job is to help students understand academic information clearly and concisely.

You can help explain information such as:
- course schedules
- grades
- GPA
- attendance
- tuition or UKT
- academic announcements
- course registration (KRS)
- academic transcripts (KHS)

Only answer based on the information provided to you.

If the requested information is not available in the provided data, clearly say that the information is not available.

Do not invent student data, grades, schedules, payments, or other academic information.

Respond in Indonesian using clear and friendly language.
"""

user_prompt_prefix = """
Here is academic information from the SIAKAD system.

Answer the student's question based only on this information.

If the information is not available, tell the student that the requested information cannot be found.

Academic data:
"""

academic_data = """
Nama: Budi Santoso
NIM: 20230001
Program Studi: Informatika
Semester: 5

Jadwal:
- Pemrograman Web: Senin, 08:00 - 10:00
- Basis Data: Selasa, 10:00 - 12:00
- Artificial Intelligence: Rabu, 13:00 - 15:00

Nilai:
- Pemrograman Web: A
- Basis Data: B+
- Artificial Intelligence: A-

UKT:
Status pembayaran: Lunas
Semester: 5
Jumlah: Rp4.500.000

Pengumuman:
Pengisian KRS semester berikutnya dibuka pada 20 September 2026.
"""

def messages_for(academic_data):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + academic_data}
    ]

messages_for(academic_data)

def summarize_academic(data):
    messages = messages_for(data)
    response = openai.chat.completions.create(model="gpt-5-nano", messages=messages)
    return response.choices[0].message.content

summarize_academic(academic_data)


def display_summary(data):
    summary = summarize_academic(data)
    display(Markdown(summary))

display_summary(academic_data)