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

// Foundations track: grades 8-12, nominal 10th-grade reading level. Same governance as modules.
const foundations = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/foundations' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    order: z.number().default(0),
    status: z.enum(['draft', 'reviewed', 'screened', 'live']).default('draft'),
    lastReviewed: z.string().optional(),
    before: z.array(z.string()).default([]),
    tool: z.string().optional(),
  }),
});

// Dated pages: figures and statuses that change. Every page carries an as-of date.
const situation = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/situation' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    asOf: z.string(),
    module: z.string().optional(),
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

export const collections = { modules, foundations, situation, glossary, sources };
