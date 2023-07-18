import multiprocessing
import eye_tracker
import face_detector
import face_landmarks
import head_pose_estimation
import mouth_opening_detector
import time

def run_python_file(module):
    module.run()

if __name__ == '__main__':
    # Create processes for each Python file
    # audio_process = multiprocessing.Process(target=run_python_file, args=(audio_part,))
    eye_process = multiprocessing.Process(target=run_python_file, args=(eye_tracker,))
    face_detector_process = multiprocessing.Process(target=run_python_file, args=(face_detector,))
    face_landmarks_process = multiprocessing.Process(target=run_python_file, args=(face_landmarks,))
    head_pose_process = multiprocessing.Process(target=run_python_file, args=(head_pose_estimation,))
    mouth_opening_process = multiprocessing.Process(target=run_python_file, args=(mouth_opening_detector,))

    # Start the processes
    # audio_process.start()
    eye_process.start()
    face_detector_process.start()
    face_landmarks_process.start()
    head_pose_process.start()
    mouth_opening_process.start()

    # Wait for user input to stop the processes
    input("Press enter to stop all processes...")
    # Terminate the processes
    # audio_process.terminate()
    eye_process.terminate()
    face_detector_process.terminate()
    face_landmarks_process.terminate()
    head_pose_process.terminate()
    mouth_opening_process.terminate()

    # Wait for all processes to complete
    # audio_process.join()
    eye_process.join()
    face_detector_process.join()
    face_landmarks_process.join()
    head_pose_process.join()
    mouth_opening_process.join()

