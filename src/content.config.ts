import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

// Lenient schemas — title required, everything else optional — so content entries
// converted from the old WordPress site never fail the build on a missing field.

const venues = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/venues' }),
  schema: z.object({
    title: z.string(),
    address: z.string().optional(),
    phone: z.string().optional(),
    website: z.string().optional(),
    capacity: z.string().optional(),
    price: z.string().optional(),
    kosher: z.string().optional(),
    summary: z.string().optional(),
    connectNote: z.string().optional(),
    image: z.string().optional(),
    gallery: z.array(z.string()).optional(),
    originalUrl: z.string().optional(),
    order: z.number().optional(),
  }),
});

const djs = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/djs' }),
  schema: z.object({
    title: z.string(),
    role: z.string().optional(),
    specialties: z.array(z.string()).optional(),
    languages: z.array(z.string()).optional(),
    photo: z.string().optional(),
    gallery: z.array(z.string()).optional(),
    videos: z.array(z.string()).optional(),
    audio: z.array(z.string()).optional(),
    summary: z.string().optional(),
    connectNote: z.string().optional(),
    originalUrl: z.string().optional(),
    order: z.number().optional(),
  }),
});

const singers = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/singers' }),
  schema: z.object({
    title: z.string(),
    role: z.string().optional(),
    specialties: z.array(z.string()).optional(),
    languages: z.array(z.string()).optional(),
    photo: z.string().optional(),
    gallery: z.array(z.string()).optional(),
    videos: z.array(z.string()).optional(),
    audio: z.array(z.string()).optional(),
    summary: z.string().optional(),
    connectNote: z.string().optional(),
    originalUrl: z.string().optional(),
    order: z.number().optional(),
  }),
});

export const collections = { venues, djs, singers };
