/** Future integration boundary. A concrete posture model has deliberately not been connected. */
export interface PostureModelAdapter {
  load(): Promise<void>;
  analyze(video: HTMLVideoElement, timestampMs: number): Promise<unknown>;
  close(): void;
}

export const postureModelAdapter: PostureModelAdapter | null = null;
