import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const modules = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/modules' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    order: z.number().default(0),
    status: z.enum(['draft', 'reviewed', 'screened', 'live']).default('draft'),
    lastReviewed: z.string().optional(),
    objectives: z.array(z.string()).default([]),
  }),
});

const glossary = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/glossary' }),
  schema: z.object({
    term: z.string(),
    source: z.string().optional(),
  }),
});

const sources = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/sources' }),
  schema: z.object({
    title: z.string(),
    authors: z.string().optional(),
    year: z.number().optional(),
    venue: z.string().optional(),
    doi: z.string().optional(),
    url: z.string().url().optional(),
    identifier: z.string().optional(),
  }),
});

export const collections = { modules, glossary, sources };
