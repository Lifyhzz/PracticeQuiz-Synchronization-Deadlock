import threading
import time

# Mendefinisikan dua sumber daya (resources) menggunakan Lock
resource_1 = threading.Lock()
resource_2 = threading.Lock()

def task_1():
    print("Task 1: Memulai eksekusi...")
    # Task 1 mengunci Resource 1
    with resource_1:
        print("Task 1: BERHASIL menahan (hold) Resource 1.")
        
        # Jeda waktu untuk memastikan Task 2 sempat berjalan dan mengunci Resource 2
        time.sleep(1) 
        
        print("Task 1: MENUNGGU (wait) Resource 2 dilepaskan oleh Task 2...")
        # Task 1 mencoba mengunci Resource 2
        with resource_2:
            print("Task 1: Berhasil mendapatkan Resource 1 dan 2. (Tidak akan tercetak)")

def task_2():
    print("Task 2: Memulai eksekusi...")
    # Task 2 mengunci Resource 2
    with resource_2:
        print("Task 2: BERHASIL menahan (hold) Resource 2.")
        
        # Jeda waktu untuk memastikan Task 1 sempat berjalan dan mengunci Resource 1
        time.sleep(1) 
        
        print("Task 2: MENUNGGU (wait) Resource 1 dilepaskan oleh Task 1...")
        # Task 2 mencoba mengunci Resource 1
        with resource_1:
            print("Task 2: Berhasil mendapatkan Resource 1 dan 2. (Tidak akan tercetak)")

if __name__ == "__main__":
    print("=== Memulai Program Simulasi Deadlock ===")
    
    # Membuat thread untuk masing-masing task
    t1 = threading.Thread(target=task_1)
    t2 = threading.Thread(target=task_2)

    # Menjalankan kedua thread secara bersamaan
    t1.start()
    t2.start()

    # Menunggu thread selesai 
    t1.join()
    t2.join()

    print("Program selesai. (Pesan ini tidak akan pernah muncul karena program terhenti akibat Deadlock).")