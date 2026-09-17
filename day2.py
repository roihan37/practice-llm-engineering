from openai import OpenAI
OLLAMA_BASE_URL = "http://localhost:11434/v1"

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
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt_prefix + academic_data},
]

ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')

def generate_response(messages):
    stream = ollama.chat.completions.create(model="qwen3:1.7b", messages=messages, stream=True)
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            yield content

for text in generate_response(messages):    
    print(text, end="", flush=True)
