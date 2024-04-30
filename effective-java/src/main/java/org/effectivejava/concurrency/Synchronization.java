package org.effectivejava.concurrency;

import java.util.concurrent.TimeUnit;

public class Synchronization {
    private static boolean stopRequested;

    public static void start() throws InterruptedException {
        Thread backThread = new Thread(() -> {
            int i = 0;
            while (!stopRequested()) {
                i++;
            }

            System.out.println("Stopped");
        });
        backThread.start();

        TimeUnit.SECONDS.sleep(2);
        requestStop();
    }

    private static synchronized void requestStop() {
        stopRequested = true;
    }

    private static synchronized boolean stopRequested() {
        return stopRequested;
    }
}
