import open3d as o3d
import multiprocessing as mp
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VisualizerWorker(mp.Process):
    def __init__(self, vis_queue):
        super(VisualizerWorker, self).__init__()
        self.vis_queue = vis_queue

    def run(self):
        while True:
            vis_task = self.vis_queue.get()
            if vis_task is None:
                break

            vis_task.run()
            vis_task.destroy_window()

        return

class MultiThreadedViewer:
    def __init__(self):
        self.visualizers = {}

    def add_geometry(self, geometry, window_name):
        if window_name in self.visualizers:
            self.visualizers[window_name].add_geometry(geometry)
        else:
            vis = o3d.visualization.Visualizer()
            vis.create_window(window_name, width=640, height=480)
            vis.add_geometry(geometry)
            self.visualizers[window_name] = vis

    def show(self, block=True):
        vis_queue = mp.JoinableQueue()
        num_workers = mp.cpu_count() * 2
        workers = [VisualizerWorker(vis_queue) for _ in range(num_workers)]
        
        for worker in workers:
            worker.start()

        for vis in self.visualizers.values():
            vis_queue.put(vis)

        for _ in range(num_workers):
            vis_queue.put(None)

        if block:
            vis_queue.join()

if __name__ == '__main__':
    # Load point clouds
    pc1 = o3d.io.read_point_cloud('../data/camera/000.pcd')
    pc2 = o3d.io.read_point_cloud('../data/camera/001.pcd')

    # Create and configure the viewer
    viewer = MultiThreadedViewer()
    viewer.add_geometry(pc1, 'Window1')
    viewer.add_geometry(pc2, 'Window2')

    # Show the viewer
    viewer.show()
