#include <iostream>
#include <random>
#include <queue>

using namespace std;

struct PCB {
  int id;
  int cpu_burst_time;
  int io_burst_time;
  int total_burst_time;
  int priority;
  string status;
};

void generate_processes(queue<PCB>& process_queue) {
  // Generate a unique process ID for each process.
  int id = 1;
  while (true) {
    PCB process;
    process.id = id++;

    // Randomly generate CPU burst time and I/O burst time for every process.
    process.cpu_burst_time = rand() % 10 + 1;
    process.io_burst_time = rand() % 10 + 1;

    // Calculate the total burst time.
    process.total_burst_time = process.cpu_burst_time + process.io_burst_time;

    // Assign a priority based on the total burst time.
    process.priority = process.total_burst_time;

    // Label the status of the process based on the ration of CPU burst time and I/O burst time.
    if (process.cpu_burst_time > process.io_burst_time) {
      process.status = "CPU Bound";
    } else {
      process.status = "I/O Bound";
    }

    process_queue.push(process);

    // If the queue is full, break out of the loop.
    if (process_queue.size() == 10) {
      break;
    }
  }
}

int main() {
  // Create a queue to store the processes.
  queue<PCB> process_queue;

  // Generate the processes.
  generate_processes(process_queue);

  // Print the processes.
  while (!process_queue.empty()) {
    PCB process = process_queue.front();
    cout << "Process ID: " << process.id << endl;
    cout << "CPU Burst Time: " << process.cpu_burst_time << endl;
    cout << "IO Burst Time: " << process.io_burst_time << endl;
    cout << "Total Burst Time: " << process.total_burst_time << endl;
    cout << "Priority: " << process.priority << endl;
    cout << "Status: " << process.status << endl;
    cout << endl;

    process_queue.pop();
  }

  return 0;
}